import streamlit as st

# Title of the Biography page
st.title("Biography of Marjon P. Vistal")

# Add a circular image (using custom HTML and CSS)
st.markdown("""
    <style>
        .circle-img {
            border-radius: 50%;
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
Hello! My name is **John Luis J. Hernandez**, and I am 18 years old. I live in Brgy. Hayanggabon, Claver, Surigao Del Norte. I love dancing, going on nature trips, and playing online games.
""")

# Early Life
st.header("Early Life")
st.write("""
I was born in Fairview, Quezon City, and raised in Brgy. Hayanggabon, Claver, Surigao Del Norte, a small town where I developed a passion for dancing and playing online games from an early age. My interest in these activities started when I was 12 years old. By the time I turned 14, I started exploring nature trips, as I felt that dancing and gaming were becoming repetitive. Nature trips offered a refreshing change and allowed me to enjoy the outdoors.
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
st.write("""
When I'm not dancing or playing online games, I enjoy **watching movies**, going on **nature trips**, and **traveling**. Spending quality time with my family is also something I cherish deeply.
""")

# Contact Information
st.header("Contact Information")
st.write("You can reach me at:")

# Display contact number
st.write("📞 **Contact Number**: +63 912 345 6789")  # Replace with your actual contact number

# Display Gmail contact link
st.write("📧 **Email**: [johnluis.hernandez@gmail.com](mailto:johnluis.hernandez@gmail.com)")  # Replace with your Gmail

# Footer
st.markdown("---")
st.write("© 2024 John Luis J. Hernandez | All rights reserved")
