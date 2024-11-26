import streamlit as st

# Title of the Biography page
st.title("Biography of John Luis Hernandez")

# Add an image
st.image("https://scontent.fcgy2-2.fna.fbcdn.net/v/t39.30808-1/466729063_1315875869574868_5258799122525142086_n.jpg?stp=dst-jpg_s200x200&_nc_cat=101&ccb=1-7&_nc_sid=50d2ac&_nc_eui2=AeHgHAq4IfUQC7mQl2nceAQ7bndqOX6-4BBud2o5fr7gEPYgHepfPusRoyra32rfG1PioTOPMUyMlbbTyz1UFFRi&_nc_ohc=Gs9D8fk99XcQ7kNvgE12Bk9&_nc_zt=24&_nc_ht=scontent.fcgy2-2.fna&_nc_gid=AErGhae3C_KRvSL_bHgB_DT&oh=00_AYDPytbLBgBYCV_RJmdB1TsPddOKvJsijm5Jz6zT4Jqglw&oe=674B301E", width=400)  # Replace with your image path or URL

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
st.write("📞 **Contact Number**: +63 9706858504")  # Replace with your actual contact number
st.write("📧 **Email**: [johnluishernandez925@gmail.com](mailto:johnluishernandez925@gmail.com)")  # Replace with your Gmail

# Footer
st.markdown("---")
st.write("© 2024 John Luis J. Hernandez | All rights reserved")

