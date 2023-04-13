# flake8: noqa
from langchain.output_parsers.regex import RegexParser
from langchain.prompts import PromptTemplate

template = """あなたはクイズで出題する問題を考える教師です。
以下の文書が与えられた場合、その文書に基づいた質問と回答を生成してください。

例のフォーマット：
<Begin Document>
...
<End Document>
QUESTION: 質問
ANSWER: 回答

これらの質問は詳細であり、明示的に文書の情報に基づいている必要があります。始めましょう！

<Begin Document>
{doc}
<End Document>"""
output_parser = RegexParser(
    regex=r"QUESTION: (.*?)\nANSWER: (.*)", output_keys=["query", "answer"]
)
PROMPT = PromptTemplate(
    input_variables=["doc"], template=template, output_parser=output_parser
)
