import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):
 # Send an HTTP GET request to the URL
    response = requests.get(url)
     # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
     # Find all instances of the "citation needed" tag
    citations_needed = soup.find_all(string="citation needed")
    
    # Count the number of citations needed
    count = len(citations_needed)
    
    return count

def get_citations_needed_report(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all elements containing the "citation needed" tag
    citations_needed_elements = soup.find_all(string="citation needed")
    
    # Initialize an empty list to store the passages
    passages = []
    
    # Iterate through the elements and get the relevant passages
    for element in citations_needed_elements:
        # Get the parent paragraph element
        parent_paragraph = element.find_parent('p')
        
        if parent_paragraph:
            passage = parent_paragraph.get_text()
            passages.append(passage)
    
    # Join the passages into a single string with line breaks
    report = '\n'.join(passages)
    
    return report

def get_citations_needed_by_section(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Initialize a dictionary to store citations by section
    citations_by_section = {}
    
    # Find all headings (you may need to adjust the tag selection)
    headings = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    
    for heading in headings:
        section_name = heading.get_text()
        
        # Find the next paragraph element after the heading
        next_paragraph = heading.find_next('p')
        
        # Check if there is a paragraph element
        if next_paragraph:
            # Find citations within this section
            citations_needed = next_paragraph.find_all(string="citation needed")
            
            # Extract and store citations for this section
            section_citations = [citation.find_parent('p').get_text() for citation in citations_needed]
            
            citations_by_section[section_name] = section_citations
    
    return citations_by_section
if __name__ == "__main__":
    url = 'https://en.wikipedia.org/wiki/Software_engineering'
    print(get_citations_needed_count(url))
    print(get_citations_needed_report(url))
    print(get_citations_needed_by_section(url))