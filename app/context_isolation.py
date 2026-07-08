"""
Intelligent Context Isolation Framework

Version : 1.0 (Rule-Based)

Purpose
-------
Identify the most relevant document(s) for a user query before
building the LLM context.

Future Versions
---------------
- Embedding-based document classification
- LLM-based intent classification
- Hybrid metadata + semantic routing
"""

from app.logger import logger


class ContextIsolationFramework:
    def __init__(self):

        # Version 1
        # Simple document knowledge base.
        # Later this will come from a document catalog/database.

        self.document_catalog = {
            "HR_Policy_3Pages.pdf": {
                "category": "Human Resources",
                "keywords": [
                    "employee",
                    "employees",
                    "hr",
                    "leave",
                    "benefits",
                    "attendance",
                    "policy",
                    "probation",
                    "recruitment",
                    "grievance",
                    "remote work",
                    "salary",
                    "performance",
                    "promotion",
                    "maternity",
                    "paternity"
                ]
            },
            "Financial_Report_3Pages.pdf": {
                "category": "Finance",
                "keywords": [
                    "finance",
                    "financial",
                    "revenue",
                    "profit",
                    "loss",
                    "investment",
                    "budget",
                    "expense",
                    "forecast",
                    "department",
                    "shareholder",
                    "cash",
                    "income",
                    "risk"
                ]
            },
            "sample.pdf": {
                "category": "Supply Chain",
                "keywords": [
                    "supply",
                    "production",
                    "planning",
                    "forecast",
                    "market",
                    "inventory",
                    "optimization",
                    "supplier",
                    "logistics",
                    "transport",
                    "shipment"
                ]
            }
        }

 
    def identify_candidate_documents(self, question: str):
        """
        Identify the most relevant documents for a query.
        Returns
        -------
        list[str] | None
        Example
        ["HR_Policy_3Pages.pdf"]
        None -> Search entire knowledge base
        """

        logger.info("=" * 60)
        logger.info("Intelligent Context Isolation")
        logger.info(f"User Query : {question}")

        question = question.lower()
        candidate_documents = []

        for document, metadata in self.document_catalog.items():
            keywords = metadata["keywords"]
            if any(keyword in question for keyword in keywords):
                candidate_documents.append(document)

        # Remove duplicates
        candidate_documents = list(set(candidate_documents))

        if candidate_documents:
            logger.info(f"Candidate Documents : {candidate_documents}")

        else:
            logger.info("No matching document identified.")
            logger.info("Falling back to full knowledge base retrieval.")

            return None
        return candidate_documents

    def filter_chunks(self, retrieved_docs, candidate_documents):
        """
        Remove chunks belonging to unrelated documents.
        """

        if candidate_documents is None:

            logger.info(
                "Context Isolation Skipped."
            )
            return retrieved_docs

        logger.info("-" * 60)
        logger.info("Filtering Retrieved Chunks...")

        filtered_docs = []
        removed_documents = []

        for doc, score in retrieved_docs:
            source = doc.metadata.get("source")
            if source in candidate_documents:
                filtered_docs.append((doc, score))
            else:
                removed_documents.append(source)

        logger.info(f"Chunks Before Filtering : {len(retrieved_docs)}")
        logger.info(f"Chunks After Filtering : {len(filtered_docs)}")
        logger.info(f"Removed Chunks : {len(retrieved_docs) - len(filtered_docs)}")

        if removed_documents:
            logger.info(f"Removed Documents : {list(set(removed_documents))}")
        logger.info("=" * 60)

        # Always return at most 3 chunks
        return filtered_docs[:3]