import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
import streamlit as st

def reset_password(authenticator, username, config):
    with st.sidebar.expander('Reset password'):
            try:
                if authenticator.reset_password(username, 'Reset password'):
                    st.success('Password modified successfully')
                    with open('config.yaml', 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
            except Exception as e:
                st.error(e)
def create_user(authenticator, config):
    with st.sidebar.expander('Create User'):
            try:
                if authenticator.register_user('Register user', preauthorization=False):
                    st.success('User registered successfully')
                    with open('config.yaml', 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
            except Exception as e:
                st.error(e)
def logout(authenticator):
    with st.sidebar:
        authenticator.logout('Logout', 'main')
def create_user(authenticator, config):
    with st.sidebar.expander('Create User'):
            try:
                if authenticator.register_user('Register user', preauthorization=False):
                    st.success('User registered successfully')
                    with open('config.yaml', 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
            except Exception as e:
                st.error(e)
def forgot_password(authenticator, config):
    with st.sidebar.expander('Forgot password'):
            try:
                if authenticator.forgot_password('Forgot password'):
                    st.success('Password reset successfully')
                    with open('config.yaml', 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
            except Exception as e:
                st.error(e)
def update_user_details(authenticator, username, config):
    with st.sidebar.expander('Update user details'):
            try:
                if authenticator.update_user_details(username, 'Update user details'):
                    st.success('Entries updated successfully')
                    with open('config.yaml', 'w') as file:
                        yaml.dump(config, file, default_flow_style=False)
            except Exception as e:
                st.error(e)


def main():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    c1,c2=st.columns([3,1])
    with c1:
        name, authentication_status, username = authenticator.login('Login', 'main')
    
    hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
    authentication_status = st.session_state["authentication_status"]
    if st.session_state["authentication_status"]:
        with st.sidebar:
                st.write(f'Welcome *{st.session_state["name"]}*')
                st.subheader('User options')
                reset_password(authenticator, username, config)
                create_user(authenticator, config)
                forgot_password(authenticator, config)
                update_user_details(authenticator, username, config)
                logout(authenticator)
            
    elif st.session_state["authentication_status"] == False:
        st.error('Username/password is incorrect')
        with c2: 
            st.image('imgs/logo.png', width=317)    
    elif st.session_state["authentication_status"] == None:
        st.warning('Please enter your username and password')
        with c2: 
            st.image('imgs/logo.png', width=317)
    return authentication_status
        
    
         

if __name__ == "__main__":
    main()