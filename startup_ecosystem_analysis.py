# models/startup_ecosystem_analysis.py

def analyze_startup_ecosystem(region="global"):
    """
    Simulates analysis of the startup ecosystem.
    In a real-world scenario, replace this static data with dynamic insights
    from sources such as Crunchbase, AngelList, etc.

    Parameters:
    - region: str, region to filter the startup ecosystem (default is "global")

    Returns:
    - List of startup insights with basic attributes.
    """
    # Dummy data representing startups and their ecosystem details
    startups = [
        {"name": "AlphaTech", "industry": "Fintech", "location": "San Francisco", "funding": "$50M", "stage": "Series B"},
        {"name": "BetaInnovations", "industry": "Healthtech", "location": "New York", "funding": "$30M", "stage": "Series A"},
        {"name": "GammaSolutions", "industry": "Artificial Intelligence", "location": "Boston", "funding": "$80M", "stage": "Series C"},
        {"name": "DeltaStart", "industry": "EdTech", "location": "London", "funding": "$20M", "stage": "Seed"},
        {"name": "Epsilon Ventures", "industry": "SaaS", "location": "Berlin", "funding": "$100M", "stage": "Series D"}
    ]
    
    # you can integrate real data sources for startup ecosystem analysis. One common approach is to use APIs like Crunchbase (or AngelList, PitchBook, etc.) to fetch live startup data
    # For now, we simply return the full list.
    return startups

if __name__ == "__main__":
    # Test the startup ecosystem analysis
    ecosystem_data = analyze_startup_ecosystem()
    print("Startup Ecosystem Analysis:")
    for startup in ecosystem_data:
        print(startup)
