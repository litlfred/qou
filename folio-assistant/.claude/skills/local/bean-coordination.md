---
name: bean-coordination
roles: [coordinator, orchestrator]
---

# Bean Coordination Skill

## Role
Coordinate teamwork and workload distribution across multiple agents using hierarchical beans (workplans/coordination).

## Instructions
1. **Hierarchical Beans**: Workplans are stored in the `.beans/` directory. Each bean represents a task or a suite of tasks.
2. **Structure**: 
   - Parent beans represent high-level goals.
   - Child beans break down the parent goal into agent-sized tasks (e.g., specific QA audits).
   - Use a 4-character ID prefix (e.g., `abcd--task-name.md`) for each bean.
3. **Linkage**: Ensure child beans reference their parent ID in the frontmatter (`parent: abcd`).
4. **Status Updates**: As agents complete tasks, they must update the `status` field of their assigned bean from `pending` to `completed` and update the `updated_at` timestamp.
5. **Sidecar QA**: For ongoing QA processes (sidecases), establish a dedicated QA bean and queue. Assign specific agents to drain the queue.
6. **CRITICAL WORKFLOW**: ALWAYS ALWAYS when starting a new goal/bean, create a feature branch and immediately push it to the remote GitHub repository. Otherwise, autonomous agents cannot coordinate effectively, resulting in a system failure.
