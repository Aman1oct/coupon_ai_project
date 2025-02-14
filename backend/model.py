import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample dataset (Replace with actual DB)
coupon_data = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "title": ["Electronics Sale", "Fashion Discount", "Grocery Offer", "Travel Deal", "Mobile Cashback"],
    "category": ["electronics", "fashion", "grocery", "travel", "mobile"]
})

def get_recommendations(user_interest):
    tfidf = TfidfVectorizer(stop_words="english")
    tfidf_matrix = tfidf.fit_transform(coupon_data["category"])
    
    similarity = cosine_similarity(tfidf_matrix, tfidf_matrix)
    similar_coupons = similarity[0].argsort()[-3:][::-1]  # Get top 3 recommendations

    return coupon_data.iloc[similar_coupons].to_dict(orient="records")
