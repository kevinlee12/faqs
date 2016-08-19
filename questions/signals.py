import os
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT


from .models import Thread

schema = Schema(title=TEXT, content=TEXT)


if not os.path.exists("index"):
    os.mkdir("index")
    ix = create_in("index", schema)
else:
    ix = open_dir("index")


writer = ix.writer()

for thread in Thread.objects.all():
    writer.add_document(title=thread.title, content=thread.response)
writer.commit()
