import psutil

SUSPICIOUS_KEYLOGGER_NAMES = [
    "keylogger", "kl.exe", "spy.exe", "logger", "keyboardhook"
]

def check_processes():
    suspicious = []
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pname = proc.info['name'].lower()
            for keyword in SUSPICIOUS_KEYLOGGER_NAMES:
                if keyword in pname:
                    suspicious.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return suspicious
