import pandas as pd
import random

def scrape_data():
    """
    Scrape data from a URL as input to an online word cloud generator (https://www.wordclouds.com/),
    like word cloud in the slide.

    This function scrapes data from a specific URL, processes it, and generates a word cloud.
    The resulting word cloud image can be obtained by visiting the provided online word cloud generator URL.

    Note: Make sure to import the required libraries (pandas and random) before using this function.

    Example:
    >>> scrape_data_and_generate_wordcloud()
    """
    # Define the URL to scrape
    url = "https://www.its.ac.id/matematika/akademik/program-studi/sarjana/"

    # Read the HTML content into a DataFrame
    df = pd.read_html(url)

    # Select specific tables by index
    idx = [8, 10]
    
    # Create an empty DataFrame to store the selected data
    df_mkp = pd.DataFrame()

    # Process and concatenate the selected tables
    for i in idx:
        df[i].columns = df[i].iloc[1]
        df[i].drop([0, 1], axis=0, inplace=True)
        df[i] = df[i][["Nama Mata Kuliah", "RMK"]]
        df_mkp = pd.concat([df_mkp, df[i]])

    # Filter data based on certain criteria
    tmp = df_mkp[df_mkp["RMK"].isin(["PMBD", "Provikom"])].copy()

    # Generate random weights for word cloud
    rnd = [random.randint(1, 10) for i in range(tmp.shape[0] * 2)]

    # Create a DataFrame with word and weight columns
    sample = pd.DataFrame({
        "weight": [random.randint(1, 10) for i in range(tmp.shape[0])],
        "word": tmp["Nama Mata Kuliah"].values,
    })

    # Save the generated data to a CSV file
    sample.to_csv("input_rmk_ilkom.csv", index=False)

    # Print the URL for the online word cloud generator
    print("Scraping Done. To generate a word cloud, visit: https://www.wordclouds.com/")


if __name__ == "__main__":
    # Call the function to scrape data
    scrape_data()
