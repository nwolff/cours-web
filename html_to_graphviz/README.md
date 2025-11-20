# cours-web

This tool parses an html page and generate a tree representation of the nested tags, in the /build directory.

To get an image you need to install graphviz, and then :

    dot -Tsvg build/html.dot.gv > build/output.svg

alternatively use the vscode graphviz plugin
