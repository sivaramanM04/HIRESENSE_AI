from langchain_community.vectorstores import FAISS


from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)


from rag.embeddings import (
    get_embeddings
)



def create_vector_db(text):


    splitter = RecursiveCharacterTextSplitter(

        chunk_size=500,

        chunk_overlap=50

    )


    chunks = splitter.split_text(
        text
    )



    db = FAISS.from_texts(

        chunks,

        get_embeddings()

    )


    return db



def search_resume(
        db,
        query
):


    docs = db.similarity_search(

        query,

        k=3

    )


    context=""


    for doc in docs:

        context += doc.page_content


    return context