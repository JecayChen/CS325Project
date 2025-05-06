import os
import tempfile
from unittest.mock import MagicMock, patch
from outputWriterHandler import OutputArticleTitles, OutputLLM
from llmprocessor import LlmProcessor

# Test for OutputArticleTitles
def test_output_article_titles(tmp_path):
    # Create a temporary input file with fake URLs
    input_file = tmp_path / "fake_urls.txt"
    input_file.write_text("https://example.com\n")

    # Create an expected output file
    output_file = tmp_path / "web_output.txt"

    # Mock the WebScraper class (assuming the scrapeTitles function returns a list of titles)
    from webscraper import WebScraper
    WebScraper.scrapeTitles = MagicMock(return_value=["Title 1", "Title 2", "Title 3"])

    # Create and run the OutputArticleTitles processor
    processor = OutputArticleTitles(str(input_file))
    processor.output(str(output_file))

    # Check that the output file exists and is not empty
    assert output_file.exists()
    content = output_file.read_text()
    assert "Title 1" in content
    assert "Title 2" in content
    assert "Title 3" in content

# Test for OutputLLM
@patch("outputWriterHandler.LlmProcessor")
def test_output_llm(mock_llm_class, tmp_path):
    # Create a temporary input file
    input_file = tmp_path / "input_titles.txt"
    input_file.write_text("Sample Article Title\n")

    # Output file
    output_file = tmp_path / "llm_output.txt"

    # Mock instance to return a fake sentiment
    mock_llm_instance = MagicMock()
    mock_llm_instance.llmSentimentQuery.return_value = "[Response to 'Sample Article Title'] => positive\n"
    mock_llm_class.return_value = mock_llm_instance  # Replace class instantiation

    # Instantiate and run
    processor = OutputLLM("mockModel", str(input_file))
    processor.output(str(output_file))

    # Assert result
    content = output_file.read_text()
    assert "positive" in content