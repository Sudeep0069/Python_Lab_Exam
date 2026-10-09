'''
Question 5: Social Media Likes 
A social media platform stores the number of likes received by five 
posts in a list. Write a function to find the post with the highest 
likes, calculate total likes, and display posts that received at least 
100 likes. 
'''
likes=[102,309,45,140,60]
def student_info(likes: list):
    posts_with_100likes=[i for i in likes if i>=100]
    return max(likes), sum(likes),posts_with_100likes
print('max likes={}\ntotal likes={}\npost with at least 100 likes={}'.format(*(student_info(likes))))