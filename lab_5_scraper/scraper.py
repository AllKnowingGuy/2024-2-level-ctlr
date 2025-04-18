"""
Crawler implementation.
"""

# pylint: disable=too-many-arguments, too-many-instance-attributes, unused-import, undefined-variable, unused-argument
import json, pathlib, re
from typing import Pattern, Union
from core_utils.config_dto import ConfigDTO
from core_utils.constants import (CRAWLER_CONFIG_PATH, NUM_ARTICLES_UPPER_LIMIT,
                                  TIMEOUT_UPPER_LIMIT, TIMEOUT_LOWER_LIMIT)

class IncorrectSeedURLError(Exception):
    """
    Raised when the seed URL is not written correctly in the configuration file.
    """
    def __init__(self, msg="Incorrect seed URL format in the config"):
        super().__init__(msg)

class NumberOfArticlesOutOfRangeError(Exception):
    """
    Raised when the number of articles is too large in the configuration file.
    """
    def __init__(self, msg="Number of articles in the config is out of range"):
        super().__init__(msg)

class IncorrectNumberOfArticlesError(Exception):
    """
    Raised when the number of articles is too small or not an integer in the configuration file.
    """
    def __init__(self, msg="Number of articles in the config is not an int or less than 0"):
        super().__init__(msg)

class IncorrectHeadersError(Exception):
    """
    Raised when the headers are not in a form of dictionary in the configuration file.
    """
    def __init__(self, msg="Headers need to be specified as a dictionary in the config"):
        super().__init__(msg)

class IncorrectEncodingError(Exception):
    """
    Raised when the encoding is not specified as a string in the configuration file.
    """
    def __init__(self, msg="Encoding should be a string in the config"):
        super().__init__(msg)

class IncorrectTimeoutError(Exception):
    """
    Raised when the timeout is too large or not a positive integer in the configuration file.
    """
    def __init__(self, msg="Timeout is incorrect or out of range in the config"):
        super().__init__(msg)

class IncorrectVerifyError(Exception):
    """
    Raised when the verify certificate value is neither True nor False in the configuration file.
    """
    def __init__(self, msg="Verify Certificate value should be True of False in the config"):
        super().__init__(msg)

class Config:
    """
    Class for unpacking and validating configurations.
    """
    path_to_config: pathlib.Path

    def __init__(self, path_to_config: pathlib.Path) -> None:
        """
        Initialize an instance of the Config class.

        Args:
            path_to_config (pathlib.Path): Path to configuration.
        """
        self.path_to_config = path_to_config
        self._validate_config_content()
        # self._extract_config_content()

    def _extract_config_content(self) -> ConfigDTO:
        """
        Get config values.

        Returns:
            ConfigDTO: Config values
        """
        with open(self.path_to_config, "r", encoding="utf-8") as file:
            config_dict = json.load(file)
        return ConfigDTO(
            config_dict["seed_urls"],
            config_dict["total_articles_to_find_and_parse"],
            config_dict["headers"],
            config_dict["encoding"],
            config_dict["timeout"],
            config_dict["should_verify_certificate"],
            config_dict["headless_mode"]
        )

    def _validate_config_content(self) -> None:
        """
        Ensure configuration parameters are not corrupt.
        """
        with open(self.path_to_config, "r", encoding="utf-8") as file:
            config_dict = json.load(file)
        if not (isinstance(config_dict["seed_urls"], list)):
            raise ValueError("Seed URLs should be a list of strings")
        for url in config_dict["seed_urls"]:
            if not re.match("https?://(www.)?", url):
                raise IncorrectSeedURLError()
        if not (isinstance(config_dict["total_articles_to_find_and_parse"], int) and
                config_dict["total_articles_to_find_and_parse"] > 0):
            raise IncorrectNumberOfArticlesError()
        if config_dict["total_articles_to_find_and_parse"] > NUM_ARTICLES_UPPER_LIMIT:
            raise NumberOfArticlesOutOfRangeError()
        if not isinstance(config_dict["headers"], dict):
            raise IncorrectHeadersError()
        if not isinstance(config_dict["encoding"], str):
            raise IncorrectEncodingError()
        if not (isinstance(config_dict["timeout"], int) and
                TIMEOUT_LOWER_LIMIT < config_dict["timeout"] < TIMEOUT_UPPER_LIMIT):
            raise IncorrectTimeoutError()
        if not isinstance(config_dict["should_verify_certificate"], bool):
            raise IncorrectVerifyError()

    def get_seed_urls(self) -> list[str]:
        """
        Retrieve seed urls.

        Returns:
            list[str]: Seed urls
        """

    def get_num_articles(self) -> int:
        """
        Retrieve total number of articles to scrape.

        Returns:
            int: Total number of articles to scrape
        """

    def get_headers(self) -> dict[str, str]:
        """
        Retrieve headers to use during requesting.

        Returns:
            dict[str, str]: Headers
        """

    def get_encoding(self) -> str:
        """
        Retrieve encoding to use during parsing.

        Returns:
            str: Encoding
        """

    def get_timeout(self) -> int:
        """
        Retrieve number of seconds to wait for response.

        Returns:
            int: Number of seconds to wait for response
        """

    def get_verify_certificate(self) -> bool:
        """
        Retrieve whether to verify certificate.

        Returns:
            bool: Whether to verify certificate or not
        """

    def get_headless_mode(self) -> bool:
        """
        Retrieve whether to use headless mode.

        Returns:
            bool: Whether to use headless mode or not
        """


def make_request(url: str, config: Config) -> requests.models.Response:
    """
    Deliver a response from a request with given configuration.

    Args:
        url (str): Site url
        config (Config): Configuration

    Returns:
        requests.models.Response: A response from a request
    """


class Crawler:
    """
    Crawler implementation.
    """

    #: Url pattern
    url_pattern: Union[Pattern, str]

    def __init__(self, config: Config) -> None:
        """
        Initialize an instance of the Crawler class.

        Args:
            config (Config): Configuration
        """

    def _extract_url(self, article_bs: BeautifulSoup) -> str:
        """
        Find and retrieve url from HTML.

        Args:
            article_bs (bs4.BeautifulSoup): BeautifulSoup instance

        Returns:
            str: Url from HTML
        """

    def find_articles(self) -> None:
        """
        Find articles.
        """

    def get_search_urls(self) -> list:
        """
        Get seed_urls param.

        Returns:
            list: seed_urls param
        """


# 10
# 4, 6, 8, 10


class HTMLParser:
    """
    HTMLParser implementation.
    """

    def __init__(self, full_url: str, article_id: int, config: Config) -> None:
        """
        Initialize an instance of the HTMLParser class.

        Args:
            full_url (str): Site url
            article_id (int): Article id
            config (Config): Configuration
        """

    def _fill_article_with_text(self, article_soup: BeautifulSoup) -> None:
        """
        Find text of article.

        Args:
            article_soup (bs4.BeautifulSoup): BeautifulSoup instance
        """

    def _fill_article_with_meta_information(self, article_soup: BeautifulSoup) -> None:
        """
        Find meta information of article.

        Args:
            article_soup (bs4.BeautifulSoup): BeautifulSoup instance
        """

    def unify_date_format(self, date_str: str) -> datetime.datetime:
        """
        Unify date format.

        Args:
            date_str (str): Date in text format

        Returns:
            datetime.datetime: Datetime object
        """

    def parse(self) -> Union[Article, bool, list]:
        """
        Parse each article.

        Returns:
            Union[Article, bool, list]: Article instance
        """


def prepare_environment(base_path: Union[pathlib.Path, str]) -> None:
    """
    Create ASSETS_PATH folder if no created and remove existing folder.

    Args:
        base_path (Union[pathlib.Path, str]): Path where articles stores
    """


def main() -> None:
    """
    Entrypoint for scrapper module.
    """


if __name__ == "__main__":
    main()
    print("Those errors above won't get you to see this line printed")
