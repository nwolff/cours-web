# cours-web

This tool parses an html page and generate a tree representation of the nested tags.

To get an image you need to install graphviz, and then :

    dot -Tsvg build/html.dot.gv > build/output.svg
