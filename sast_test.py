# Intentionally vulnerable file for SAST testing. Do not use in production.
import os

password = "hardcoded-secret-123"
eval(os.environ.get("CMD", "1+1"))
