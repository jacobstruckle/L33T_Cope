import argparse
from typing import List


class Solution:
    """
    A class to calculate the h-index of a researcher based on their citation counts.
    """

    def hIndex(self, citations: List[int]) -> int:
        """
        Calculates the h-index of a researcher.

        Args:
            citations (List[int]): List of citation counts.

        Returns:
            int: The h-index value.
        """
        if not citations:
            return 0

        sorted_citations = sorted(citations, reverse=True)
        for i, citation in enumerate(sorted_citations):
            if citation < i + 1:
                return i
        return len(sorted_citations)


def main():
    """
    Main function to handle user interaction through the terminal.
    """
    parser = argparse.ArgumentParser(
        description="Calculate the h-index based on a list of citation counts."
    )
    parser.add_argument(
        "citations",
        nargs="*",
        type=int,
        help="A list of integers representing citation counts (e.g., 3 0 6 1 5).",
    )
    args = parser.parse_args()

    if not args.citations:
        print("Error: No citation data provided.")
        print("Usage: python h_index.py <citation1> <citation2> ... <citationN>")
        return

    solution = Solution()
    h_index = solution.hIndex(args.citations)
    print(f"The calculated h-index is: {h_index}")


if __name__ == "__main__":
    main()