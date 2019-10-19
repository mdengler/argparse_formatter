from argparse import HelpFormatter
import re
import textwrap

class ParagraphFormatter(HelpFormatter):
    """
    An argparse formatter that preserves paragraphs
    (text separated by a blank line)
    """

    def __init__(self, *args, **kwargs):
        self.psep = "\n\n"
        self.psepre = "\n\\s*\n"
        super().__init__(*args, **kwargs)

    def _fill_text(self, text, width, indent):
        formatted = []
        #for paragraph in text.split(self.psep):
        for paragraph in re.split(self.psepre, text):
            paragraph = self._whitespace_matcher.sub(" ", paragraph).strip()
            formatted.append(
                textwrap.fill(
                    paragraph,
                    width,
                    initial_indent=indent,
                    subsequent_indent=indent,
                )
            )

        return self.psep.join(formatted)

    def _split_lines(self, text, width):
        formatted = []
        for paragraph in re.split(self.psepre, text):
            paragraph = self._whitespace_matcher.sub(" ", paragraph).strip()
            if formatted:
                formatted.append("")
            formatted += textwrap.wrap(paragraph, width)

        return formatted
