# api/app.py


from flask import Flask, jsonify, request
from data_ingestion.fetch_data import fetch_news_data
from data_ingestion.competitor_tracking import fetch_competitor_news
from models.sentiment_analysis import analyze_sentiment
from models.industry_forecasting import forecast_industry
from models.startup_ecosystem_analysis import analyze_startup_ecosystem

app = Flask(__name__)

# Replace with your actual NewsAPI key or load it from an environment variable
API_KEY = "Your API KEY"  

# Example competitor names
COMPETITORS = ["Competitor A", "Competitor B"]

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Market Intelligence API!"

@app.route('/market-trends', methods=['GET'])
def market_trends():
    try:
        news_data = fetch_news_data(API_KEY)
        articles = news_data.get('articles', [])
        results = []
        for article in articles:
            title = article.get('title', '')
            description = article.get('description', '')
            combined_text = f"{title}. {description}"
            sentiment = analyze_sentiment(combined_text)
            results.append({
                "title": title,
                "description": description,
                "sentiment": sentiment
            })
        return jsonify({"market_trends": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/competitors', methods=['GET'])
def competitor_tracking():
    try:
        competitor_data = {}
        for competitor in COMPETITORS:
            news = fetch_competitor_news(API_KEY, competitor)
            articles = news.get("articles", [])
            results = []
            for article in articles:
                title = article.get('title', '')
                description = article.get('description', '')
                combined_text = f"{title}. {description}"
                sentiment = analyze_sentiment(combined_text)
                results.append({
                    "title": title,
                    "description": description,
                    "sentiment": sentiment
                })
            competitor_data[competitor] = results
        return jsonify({"competitor_tracking": competitor_data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/industry-forecast', methods=['GET'])
def industry_forecast():
    try:
        # Accept query parameters for industry and forecast periods (defaults provided)
        industry = request.args.get("industry", "Tech")
        periods = int(request.args.get("periods", 30))
        forecast_data = forecast_industry(industry, periods)
        return jsonify({"industry_forecast": forecast_data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/startup-ecosystem', methods=['GET'])
def startup_ecosystem():
    try:
        # Accept an optional query parameter for region (default is "global")
        region = request.args.get("region", "global")
        ecosystem_data = analyze_startup_ecosystem(region)
        return jsonify({"startup_ecosystem": ecosystem_data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)

