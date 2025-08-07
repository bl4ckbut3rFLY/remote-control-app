def get_system_info():
    return """
import platform
info = {
    'system': platform.system(),
    'node': platform.node(),
    'release': platform.release(),
    'version': platform.version(),
    'machine': platform.machine(),
    'processor': platform.processor()
}
print(info)
"""

def show_custom_notification(text):
    return f"""
from plyer import notification
notification.notify(title='Remote Message', message='{text}')
"""

def execute_shell_command(cmd):
    return f"""
import subprocess
output = subprocess.getoutput('{cmd}')
print(output)
"""
