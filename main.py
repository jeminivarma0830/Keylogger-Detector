from detector import check_processes

def main():
    print("🔍 Keylogger Detection Tool Running...\n")
    suspicious = check_processes()
    if suspicious:
        print("⚠️ Suspicious processes detected:")
        for proc in suspicious:
            print(f"PID: {proc['pid']} | Name: {proc['name']}")
    else:
        print("✅ No suspicious keylogger processes found.")

if __name__ == "__main__":
    main()
