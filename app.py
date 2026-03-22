import streamlit as st
import random
import matplotlib.pyplot as plt
import time

# Page config
st.set_page_config(page_title="EV Battery AI", layout="wide")

# Title
st.title("🚗 Smart EV Battery Guardian 🔋")
st.caption("AI-powered battery monitoring and self-healing system")

# Sidebar (Control Panel)
st.sidebar.title("⚙️ Control Panel")
num_cells = st.sidebar.slider("Number of Cells", 3, 10, 5)
temperature = st.sidebar.slider("Temperature (°C)", 0, 50, 30)
mode = st.sidebar.selectbox("Driving Mode", ["Eco", "Normal", "Sport"])

# Simulate battery health
base_health = 100

if mode == "Sport":
    base_health -= 10
elif mode == "Eco":
    base_health += 5

if temperature > 40:
    base_health -= 15
elif temperature < 10:
    base_health -= 5

# Top metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Battery Health", f"{base_health}%", "-2%")

with col2:
    st.metric("Estimated Range", f"{base_health * 1.2:.0f} km")

with col3:
    st.metric("Temperature", f"{temperature}°C")

# Cell status
st.subheader("🔋 Cell Status")

cell_healths = []

for i in range(num_cells):
    health = random.randint(max(40, base_health - 30), base_health)
    cell_healths.append(health)

    if health > 80:
        st.success(f"Cell {i+1}: Healthy 🟢 ({health}%)")
    elif health > 60:
        st.warning(f"Cell {i+1}: Weak 🟡 ({health}%)")
    else:
        st.error(f"Cell {i+1}: Critical 🔴 ({health}%)")

# Self-healing
if st.button("Start Self-Healing"):
    st.info("♻️ Healing in progress...")

    for i in range(len(cell_healths)):
        if cell_healths[i] < 70:
            cell_healths[i] += 10

    time.sleep(1)
    st.success("✅ Healing Complete!")

# Graph
st.subheader("📊 Battery Performance")

fig, ax = plt.subplots()
ax.plot(cell_healths, marker='o')
ax.set_xlabel("Cell Number")
ax.set_ylabel("Health (%)")
ax.set_title("Battery Health Across Cells")

st.pyplot(fig)