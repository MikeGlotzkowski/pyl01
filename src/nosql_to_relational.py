import database as db
import models.Root as Root

def convert_document_to_data_classes(document):
    root = Root.Root.from_dict(document)
    return root

connection = db.get_connection()
collection = db.get_connection_to_collection(connection, "challenger")
document = db.get_one_document_of_collection(collection)
data = convert_document_to_data_classes(document)
print(data)
