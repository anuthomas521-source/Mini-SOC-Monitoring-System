

# MINI SOC MONITORING SYSTEM
# Day 4 - Threat Detection

file_path = "logs/auth.log"

# Step 1: Read authentication logs
with open(file_path, "r") as file:
    logs = file.readlines()

# Step 2: Create counters
successful_logins = 0
failed_logins = 0

# Store failed attempts for each IP
failed_attempts = {}

# Step 3: Analyze each log entry
for line in logs:

    if "Accepted password" in line:
        successful_logins += 1

    elif "Failed password" in line:
        failed_logins += 1

        # Extract username and IP address
        parts = line.split()

        username = parts[7]
        ip_address = parts[9]

        # Count failed attempts per IP
        if ip_address in failed_attempts:
            failed_attempts[ip_address] += 1
        else:
            failed_attempts[ip_address] = 1

# Step 4: Display monitoring results
print("====================================")
print("      MINI SOC MONITORING SYSTEM")
print("====================================")

print("Total log entries:", len(logs))
print("Successful logins:", successful_logins)
print("Failed login attempts:", failed_logins)

print("\nFailed Attempts by IP Address:")

for ip, count in failed_attempts.items():
    print(ip, ":", count, "failed attempts")

# Step 5: Detect suspicious IP addresses
print("\n====================================")
print("        THREAT DETECTION ALERTS")
print("====================================")

threshold = 3
alerts_found = False

for ip, count in failed_attempts.items():

    if count >= threshold:
        print("[ALERT] Suspicious activity detected!")
        print("IP Address:", ip)
        print("Failed Attempts:", count)
        print("Possible Threat: Brute-force attempt\n")

        alerts_found = True

if not alerts_found:
    print("No suspicious login activity detected.")

print("====================================")
print("Threat monitoring completed!")
