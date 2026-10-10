#!/bin/bash
FILE="quantum-observable-universes_seq2.md"
PROMPT="Read the file at /Users/litlfred/space_cats/qou/amalgamated_input/$FILE.
Rewrite its prose across all blocks to flow smoothly and linearly according to the Milnor standard (H1-H8: Economy, Concrete before abstract, Why precedes What, Uncluttered notation, Linear argument, Prose carries argument, Surgical cleanliness, Respect for reader) and the 'milnor-brevity' rules.
CRITICAL RULE 1: You MUST strictly preserve all <!-- FILE_START: ... --> and <!-- FILE_END: ... --> markers exactly as they appear. Do not delete them.
CRITICAL RULE 2: You must write the edited text to /Users/litlfred/space_cats/qou/amalgamated_done/$FILE.
CRITICAL RULE 3: You must write a JSON audit report to /Users/litlfred/space_cats/qou/amalgamated_done/$FILE.qa.json with your audit notes under the 'milnor-amalgamated-flow' criterion:
{
  \"criteria\": {
    \"milnor-amalgamated-flow\": [
      {
        \"result\": \"pass\",
        \"notes\": \"Your detailed audit report goes here...\",
        \"reviewed_at\": \"2026-07-06T22:30:00Z\",
        \"reviewer\": { \"kind\": \"agent\", \"id\": \"milnor-editor\", \"version\": \"v1\" }
      }
    ]
  }
}
Execute the file writes and report done."

agy --dangerously-skip-permissions -p "$PROMPT"
