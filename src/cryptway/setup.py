from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

print(pwd_context.hash("cryptway_sk_ddf3708c9e0c50f70c60dea902f158859e988b123e6443b0bd503a59c53821e8"))