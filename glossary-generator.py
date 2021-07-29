
import os
import re

glossdir = 'content/glossary'

with open(glossdir+'.md', 'w') as f:
    f.write('''
---
title: "Glossary"
---

# Glossary


''')
    terms = {}
    for fname in sorted(os.listdir(glossdir)):
        if fname.endswith('.md'):
            tag = fname[:-3]
            term = tag.replace('-', ' ').title()
            terms[term] = tag

    print(terms.items())

    for fname in sorted(os.listdir(glossdir)):
        if fname.endswith('.md'):
            tag = fname[:-3]
            term = tag.replace('-', ' ').title()
            print(term)
            # f.write(f'\n\n### [{term}](/glossary/{tag})\n\n')
            f.write(f'\n\n### {term}\n\n')
            with open(os.path.join(glossdir, fname), 'r') as g:
                text = g.read()
                for term2, tag2 in terms.items():
                    if term2 == term:
                        continue
                    # text = re.sub(f"({term2})", f"[\1](#{tag2})", text, re.IGNORECASE)
                    print('\t', term2, tag2)
                    text = re.sub(f"({term2}s?)", r'[\1]'+f"(#{tag2})", text, flags=re.IGNORECASE)

                f.write(text)



