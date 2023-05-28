from query.vortex_query import VortexQuery


def main():
    vortex_query = VortexQuery()

    while True:
        print()
        question = input("Question: ")

        answer, source = vortex_query.ask_question(question)

        print("\n\nSources:\n")
        for document in source:
            print(f"Page: {document.metadata['page_number']}")
            print(f"Text chunk: {document.page_content[:160]}...\n")
        print(f"Answer: {answer}")


if __name__ == "__main__":
    main()
