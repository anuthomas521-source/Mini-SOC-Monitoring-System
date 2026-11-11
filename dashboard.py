
import streamlit as st

# Dashboard settings
st.set_page_config(
    page_title="Mini SOC Dashboard",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Mini SOC Monitoring Dashboard")
st.write("Authentication Log Monitoring and Threat Detection")

# Read authentication logs
file_path = "logs/auth.log"

with open(file_path, "r") as file:
    logs = file.readlines()

# Count login activities
successful_logins = 0
failed_logins = 0
failed_attempts = {}

for line in logs:

    if "Accepted password" in line:
        successful_logins += 1

    elif "Failed password" in line:
        failed_logins += 1

        parts = line.split()
        username = parts[7]
        ip_address = parts[9]

        failed_attempts[ip_address] = (
            failed_attempts.get(ip_address, 0) + 1
        )

# Dashboard metrics
total_logs = len(logs)

col1, col2, col3 = st.columns(3)

col1.metric("Total Log Entries", total_logs)
col2.metric("Successful Logins", successful_logins)
col3.metric("Failed Login Attempts", failed_logins)

st.divider()

# Failed attempts by IP
st.subheader("Failed Login Attempts by IP Address")

if failed_attempts:
    st.bar_chart(failed_attempts)
else:
    st.info("No failed login attempts found.")

# Threat detection
st.subheader("🚨 Threat Detection Alerts")

threshold = 3
alerts_found = False

for ip, count in failed_attempts.items():

    if count >= threshold:
        st.error(
            f"Suspicious IP: {ip} | "
            f"{count} failed attempts | "
            "Possible brute-force activity"
        )
        alerts_found = True

if not alerts_found:
    st.success("No suspicious login activity detected.")

st.divider()


# Security Event Table
st.subheader("📋 Security Event Log")

event_data = []

for line in logs:
    if "Accepted password" in line:
        event_data.append({
            "Event": "Successful Login",
            "Log Details": line.strip(),
            "Status": "Normal"
        })

    elif "Failed password" in line:
        event_data.append({
            "Event": "Failed Login",
            "Log Details": line.strip(),
            "Status": "Suspicious"
        })

if event_data:
    st.dataframe(event_data, use_container_width=True)

st.caption("Mini SOC Monitoring System | Learning Project")
