---
doc_id: arxiv-2605.22763v1
doc_title: "Advancing Mathematics Research with AI-Driven Formal Proof Search"
section_id: sec-007-further-details-on-alphaproof-nexus-agents
section_title: "Further Details on AlphaProof Nexus Agents"
section_number: null
pages: 18-22
source_pdf: 2605.22763v1.pdf
source_sha256: 1fe6b92bb5eb0b45
toc_source: outline
doc_brief: "Advancing Mathematics Research with AI-Driven Formal Proof Search — 29 sections: Front matter; Introduction; AlphaProof Nexus"
---
1
# Main Loop
2
initial_sketch = lean_compiler.check(initial_file)
3
final_sketch = prover_subagent(initial_sketch)
4
5
# Basic prover subagent
6
def prover_step(sketch):
7
session = LlmSketcher(sketch) # Start an LLM session
8
while tool_call := session.recv():
9
if tool_call.is_search_replace():
10
sketch, feedback = search_replace_then_compile(sketch, tool_call)
11
session.send(feedback)
12
13
if lean_compiler.verify_integrity(sketch): # Check for hacks
14
return sketch
15
16
def prover_subagent(initial_sketch):
17
sketch = initial_sketch
18
while within_budget() and sketch.contains_sorry():
19
if new_sketch := prover_step(sketch):
20
sketch = new_sketch
21
return sketch
Figure 4 | Pseudocode for the basic agent (A). A prover subagent executes a sequence of
steps in a loop. Each step is a conversation with a LLM instance (Gemini 3.1 Pro). During
this conversation, the subagent can view a Lean file and apply search-replace edits. After
each change, the Lean compiler provides feedback, such as compilation errors. As for agent
(D), we check for the integrity of the final sketch once the conversation is over. 𝑁subagents
run independently in parallel and stop as soon as one of them found a valid proof.
Basic Agent.
The pseudocode for the basic agent (A) is shown in Figure 4. The agent
operates 𝑁independent subagents that share no state. All subagents start with the same
initial proof sketch. As soon as one subagent finds a proof, all others are terminated.
Each subagent implements a Ralph loop [31] consisting of a sequence of episodes. The
full prompt is shown in Figure 8. Within each episode, the subagent runs a multi-turn
session with an access to a search_replace tool. After each edit, the Lean code is compiled
and compiler feedback is passed back to the model. When the subagent ends an episode,
the code is validated using SafeVerify [24], which checks the proof against the theorem
specification and guards against environment exploits (e.g., axiom injection). If validation
succeeds and the proof is sorry-free, the proof is returned. If sorry remains, the subagent
summarizes lessons learned in a comment and begins the next episode from the current
sketch. If validation fails, the subagent reverts to the previous sketch.
Full-featured Agent.
The pseudocode for the full-featured agent (D) is shown in Fig-
ure 5. The evolutionary process is orchestrated by a controller, which executes a continuous,
18
Advancing Mathematics Research with AI-Driven Formal Proof Search
1
# Main Loop
2
initial_sketch = lean_compiler.check(initial_file)
3
population.initialize(initial_sketch)
4
launch prover_subagents(N, population) # Create prover agents
5
launch rater_subagents(M, population) # Create rater agents
6
await population.contains_sorry_free_proof()
7
8
# Prover subagent, run asynchronously
9
def prover_step(sketch):
10
session = LlmSketcher(sketch) # Start an LLM session
11
while tool_call := session.recv():
12
if tool_call.is_alphaproof(): # Call AlphaProof
13
proofs = [alphaproof.solve(g) for g in unsolved_goals(sketch)]
14
sketch, feedback = incorporate_proofs(proofs, sketch)
15
elif tool_call.is_search_replace(): # Call search-and-replace
16
sketch, feedback = search_replace_then_compile(sketch, tool_call)
17
session.send(feedback)
18
if lean_compiler.verify_integrity(sketch): # Check for hacks
19
population.add(sketch)
20
return not sketch.contains_sorry()
21
return False
22
23
def prover_subagent():
24
while within_budget():
25
sketch = population.sample(strategy=p_ucb) # Sample a sketch
26
if prover_step(sketch):
27
break
28
29
# Rater agent, run asynchronously
30
def rater_subagent():
31
s1, ..., sP = sketch_db.get_sketches_for_ranking()
32
ranks = llm_rater.rank(s1, ..., sP)
33
sketch_db.update_elo(ranks)
Figure 5 | Pseudocode for the main components of the full-featured agent (Agent (D)).
The main loop creates a pool of asynchronous prover subagents and raters and awaits the
creation of a full (sorry-free) proof. At each step, a prover subagent uses the P-UCB strategy
to sample a parent sketch from the population and initiates a stateful conversation with
a LLM instance (Gemini 3.1 Pro). The agent has access to two tools: AlphaProof and a
structured search-and-replace operation. The results of these tool calls provide context for
the subsequent turn. Once the conversation concludes, the resulting sketch is added to the
population only if it compiles successfully and the original theorem remains uncompromised.
Concurrently, each rater_agent samples 𝑃sketches, uses a LLM (Gemini 3.0 Flash) to
determine which is the most promising, and updates the Elo scores used for P-UCB sampling.
We set 𝑃= 7 in all the experiments.
19
Advancing Mathematics Research with AI-Driven Formal Proof Search
asynchronous loop. At each step, the controller performs the following stages:
1. Database sampling: The controller selects a root proof sketch 𝑆root by sampling from
the database, along with 𝑀= 2 auxiliary inspiration sketches 𝑆insp. The selection strat-
egy balances exploitation of high-rated sketches with exploration of diverse candidates
(see “Population Database and Matchmaking”).
2. Prompt construction: A prompt X is assembled to guide the LLM. It integrates the
formal problem specification, the Lean source code and natural language plan of 𝑆root,
and structured feedback derived from AlphaProof’s previous attempts on {𝑆insp}. As in
AlphaEvolve, the controller encourages diversity by stochastically injecting instructions
such as “decompose unsolved goals,” “combine ideas from prior attempts,” or “try a
completely new approach.”
3. Prover subagent: The assembled prompt X is dispatched to the LLM (Gemini 3.1
Pro), initiating a multi-turn episode. To scale to large Lean files, the subagent outputs
mutations via a search_replace tool in a compact diff format rather than rewriting
the entire file. The subagent can also query AlphaProof to test specific subgoals mid-
episode; the feedback indicates whether the goal was proven, disproven, or unresolved.
To manage compute, each episode is restricted to a maximum of 5 AlphaProof queries
and 90 search-and-replace edits. At the conclusion of the episode, the generated
sketch undergoes a sandbox check that permits sorry placeholders but verifies that
the original target theorem statement was not altered.
4. Validation: Once the candidate sketch 𝑆′ passes the sandbox check, it undergoes formal
validation. The system extracts all remaining sorry subgoals and cross-references
them against a global goal cache using a deep hash of their exact Lean state (see “Global
Goal Caching”). If a subgoal was previously resolved, the proof is retrieved immediately;
otherwise, it is dispatched to AlphaProof. If AlphaProof closes all remaining goals,
the fully assembled, sorry-free proof is passed to SafeVerify [24] for final validation,
ensuring the proof compiles and that no disallowed axioms (including sorryAx) were
introduced. If any subgoals remain unresolved, 𝑆′ is registered with its remaining
sorry placeholders.
5. Database registration: The candidate 𝑆′, along with per-subgoal feedback from Al-
phaProof, is registered in the database. Its fitness is then determined asynchronously
via Elo matchmaking.
AlphaProof has a Test-Time Reinforcement Learning (TTRL) mode in which it learns to
solve a problem by solving its AI-generated variants at inference time; however, we prioritize
the use of compute for LLM inference and run AlphaProof in its low-compute tree search
inference mode.
Population Database and Matchmaking.
Unlike systems where numerical fitness can be
directly computed (e.g., empirical runtime), formal proof evaluation yields only discrete
signals: whether the code compiles and whether the proof is complete. Agent (D) overcomes
this by decoupling generation from fitness assignment, using LLM-based relative review to
evaluate the promise of incomplete sketches.
20
Advancing Mathematics Research with AI-Driven Formal Proof Search
Elo-based Rating.
Asynchronous rater agents (Gemini 3.0 Flash) continuously sample sets
of 𝑃= 7 sketches from the database for pairwise “matches.” We found 𝑃= 7 to provide a
good trade-off between information per LLM call and input context size. Each rater produces
a relative ranking by evaluating the clarity of the proof strategy, the plausibility of remaining
goals, and the mathematical novelty of the approach.
We model match outcomes using a Plackett-Luce distribution [47, 41], in which each
sketch 𝑠has a latent strength parameter 𝜆𝑠.
We place a hierarchical prior 𝑝(𝜆𝑠|𝑟𝑠) =
Gamma(1, 𝑟𝑠) with rate parameter 𝑟𝑠distributed as 𝑝(𝑟𝑠) = Gamma(1, 1). This distribution
has heavier tails than a simple Gamma over 𝜆𝑠while keeping the distributions conditionally
conjugate; we expect the choice of hyperparameters to have a relatively small impact.
We infer sketches’ posterior strengths using a Gibbs sampling procedure [14]. For each
sketch 𝑠, we draw 𝐼Gibbs samples {𝜆(𝑖)
𝑠}𝐼
𝑖=1 from the posterior distribution of that sketch’s
strength parameter, obtained after drawing 𝐵burn-in samples (we set 𝐼= 1000 and 𝐵= 200
based on an experiment with synthetic data). We then use the posterior sample mean
𝜆mean
𝑠
= 1
𝐼
Í
𝑖𝜆(𝑖)
𝑠
to obtain the sketch’s Elo score as
Elo𝑠= 1200 + 400 log10 𝜆mean
𝑠
.
To obtain the set of 𝑃sketches for each match, we use a Thompson sampling strategy that
repeatedly takes an independent sample 𝜆𝑠for each sketch and chooses the sketch with the
highest value. In practice, we obtain the independent samples via Gibbs sampling, retaining
only every 25-th sample in order to mitigate in-chain correlation. This is sampling with
replacement, so the same sketch may appear more than once. After sampling exactly 𝑃times,
we remove duplicate sketches from the chosen set, replacing them with the sketches with
the highest posterior sample variance 𝜆var
𝑠.
Occasionally the LLM raters may output ties between the input sketches. Since the
Plackett-Luce model does not consider ties, we break ties randomly by sampling from the
model.
Evolutionary Selection.
During the sampling phase, the controller selects “parent” sketches
using the Predictor + Upper Confidence Bound (P-UCB) formula. To focus the search and
reduce computational overhead, the sampler first filters the population to the top 64 highest-
scoring sketches based on their current Elo ratings. For these top candidates, the Elo ratings
are normalized to a range of [0, 1] to yield a base score 𝑞. The final P-UCB score for each
sketch is then computed as:
score = 𝑞+ 𝑐
√︁Í𝑉𝑖
𝑣+ 1
where 𝑣is the number of times the specific sketch has been visited (sampled), Í𝑉𝑖is the
total number of visits across the filtered population, and 𝑐is a tunable exploration constant
(set at 0.2 for this work). This mechanism prioritizes the exploitation of the most promising
sketches – those within the elite top-64 threshold – while the UCB exploration bonus ensures
adequate exploration of newly promoted or infrequently sampled candidates within that
elite tier, preventing the search from collapsing into a single, suboptimal lineage. The values
𝑐= 0.2 and top-64 were chosen empirically based on observed performance.
21
Advancing Mathematics Research with AI-Driven Formal Proof Search
Global Goal Caching and Incorporation.
Independent proving agents can generate the
same goals to dispatch to AlphaProof. For efficiency, Agent (D) implements a global goal
cache within the database. When a sketch is parsed, the system computes a deep hash of the
exact formal Lean context and target for every generated subgoal (the goal_id). Before
querying AlphaProof, the validator checks this cache. If a specific subgoal’s state was already
proved or formally disproved in any prior sketch across the population, the result – along
with the specific tactic sequence or value function – is retrieved and incorporated into the
current sketch. Novel subgoals are batched and dispatched concurrently to AlphaProof via
non-blocking remote procedure calls (RPCs), and their subsequent results are cached to
accelerate future generations.
AlphaProof Budget.
When a novel subgoal is evaluated, AlphaProof executes a formal
tree search to discover a proof or disproof. To prevent the system from stalling on intractable
or hallucinated goals, AlphaProof operates under a strict computational budget, typically
restricted to 400 simulations and bounded by a hard RPC timeout. We compile AlphaProof’s
response into textual feedback in case it cannot solve a subgoal. This feedback is then
associated with this particular subgoal and rendered in the corresponding prompt sketches.
Implementation.
The entire AlphaProof Nexus infrastructure is implemented in Python,
utilizing the asyncio framework. The evolutionary controller in Agent (D) runs an event
loop that distributes work across asynchronous threads for generation, validation, and Elo
rating. Formal validation and compilation are executed inside isolated sandboxes (Docker
instances) running Lean v4.27 and Pantograph [5]. This ensures that generated code is
type-checked in a secure, stateful environment without risking execution of malicious code.
The LLM backend leverages an ensemble of models: Gemini 3.1 Pro is used for the complex
reasoning required in the multi-turn proving agent, while the faster Gemini 3.0 Flash is
deployed for high-throughput match rating and evaluation synthesis.
