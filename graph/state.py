from typing import TypedDict, Optional

# this define the structure of our shared data across different agents and steps in the research process. It includes fields for task ID, query, max subtopics, plan, search results, analysis, report, citations, review feedback, revision count, max revisions, verdict, logs, status, and error. This structured format allows us to maintain a consistent state throughout the research lifecycle and facilitates communication between different components of the system.
class ResearchState(TypedDict):
    task_id: str
    query: str
    max_subtopics: int

    plan: list[str]
    search_results: dict[str, str]

    analysis: str
    report: str
    citations: list[str]

    review_feedback: str
    revision_count: int
    max_revisions: int
    verdict: str

    logs: list[dict]

    status: str
    error: Optional[str]