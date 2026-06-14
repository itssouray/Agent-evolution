from dataclasses import dataclass, field


@dataclass
class ReplanningState:

    goal: str

    original_plan: list[str] = field(default_factory=list)

    pending_tasks: list[str] = field(default_factory=list)

    completed_tasks: list[str] = field(default_factory=list)

    failed_tasks: list[dict] = field(default_factory=list)

    results: dict[str, str] = field(default_factory=dict)

    replan_count: int = 0

    max_replans: int = 3