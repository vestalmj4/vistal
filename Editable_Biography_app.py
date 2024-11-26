import streamlit as st

# Title of the Biography page
st.title("Biography of Marjon P. Vistal")

# Add a circular image (using custom HTML and CSS)
st.markdown("""
    <style>
        .circle-img {
            border-radius: 25%;
            width: 200px;  /* You can adjust the size here */
            height: 200px;  /* Make sure it's square to maintain the circular shape */
            object-fit: cover;  /* Ensures the image fits well inside the circle */
        }
    </style>
    <img src="https://scontent.fcgy2-2.fna.fbcdn.net/v/t1.15752-9/462575641_1661064754823752_7180113722861028547_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=9f807c&_nc_eui2=AeFNHJIDxdEskvLeDPzup0uu7vCZ-A4nWT3u8Jn4DidZPbRER4lRkHQ2XfAjFpG8JnJViL0VsiXnfk4j4SL22RqF&_nc_ohc=lqAIIcgXP1EQ7kNvgEeRNpv&_nc_zt=23&_nc_ht=scontent.fcgy2-2.fna&oh=03_Q7cD1QGP2t4EaJDF3IwARKETwjHVT7zjnipJlRQkrMMqb9m0hA&oe=676CF5E9" class="circle-img">
""", unsafe_allow_html=True)  # Replace with your image path or URL

# Add some text and subheadings
st.header("About Me")
st.write("""
Hello! My name is **Marjon P.Vistal I live in brgy, Hayanggabon, claver, Surigao Del Norte, I love playing basketball 
""")

# Early Life
st.header("Early Life")
st.write("""
I was born in Taligaman, Butuan City, and raised in Brgy. Hayanggabon, Claver, Surigao Del Norte, a small town where I developed my skills to play baketball and I really love this sport, somtimes i'm watching anime to relax.
""")

# Education
st.header("Education")
st.write("""
I graduated from Taganito National High School. High school was an exciting time for me, as it gave me the chance to dive deeper into subjects that fascinated me, while also challenging me to expand my knowledge in new areas. I realized that education isn't just about memorizing facts; it's about learning how to apply that knowledge in the real world.
""")

# Career
st.header("Career")
st.write("""
After graduating from high school, I enrolled at Surigao del Norte State University (SNSU) to pursue a degree in Computer Engineering. This marks the beginning of my journey toward a career in technology, where I hope to contribute to solving real-world problems using my skills and knowledge.
""")

# Hobbies and Interests
st.header("Hobbies and Interests")
st.write(" when i'm not playing basketball, im waching anime and hanging out with my friends. .
""")

# Contact Information
st.header("Contact Information")
st.write("You can reach me at:")

# Display contact number
st.write("📞 **Contact Number**: +63 912 557 1086")  # Replace with your actual contact number

# Display Gmail contact link
st.write("📧 **Email**: [vestalmj4@gmail.com](mailto:vestalmj4gmail.com)")  # Replace with your Gmail

# Footer
st.markdown("---")
st.write("© 2024 Marjon P. vistal | All rights reserved")
