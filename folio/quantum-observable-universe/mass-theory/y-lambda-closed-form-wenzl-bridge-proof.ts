import { proof } from "../../schema/builders";

export default proof({
  label: "prf:y-lambda-closed-form-wenzl-bridge",
  title: "Proof of y lambda closed form wenzl bridge",
  uses: ["prop:y-lambda-closed-form-wenzl-bridge"],
  authorNotes: [
    {
      kind: "deprecated",
      date: "2026-08-09",
      body: "Table 2 previously carried a numerical\nwitness-versus-bridge comparison agreeing to $\\sim 10^{-16}$ — $y_{(3)} =\n0.41539579$, $y_{(2,1)} = 0.28092963$, $y_{(1^3)} = 0.02274495$, and at $n = 4$\nthe negative entry $y_{(1^4)} = -0.00084253$. Both legs of that comparison were\n**convention C**, excised by the owner ruling of 2026-08-09, so the agreement\ncertified nothing about the production trace. The independent numerical leg has\nnot been re-run: `computations/wedderburn_jones_markov.py::y_lambda_at` is still\nconvention C (and truncates to 30 significant digits against a 50-dps floor),\nand regenerating it is a producer change, not an edit.",
    },
  ],
});
