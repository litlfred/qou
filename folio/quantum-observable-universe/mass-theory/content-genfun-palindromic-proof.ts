import { proof } from "../../schema/builders";

export default proof({
  label: "prf:content-genfun-palindromic",
  title:
    "Proof that $C_n(q)$ is palindromic and bar-even via the conjugation anti-involution",
  uses: [
    "prop:content-genfun-palindromic",
  ],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): **Machine verification.** The two structural steps ... are proved for arbitrary finite index sets in `QOU.AntiInvolutionPalindrome`. The Lean sibling checks the $n=4$ instance concretely." },
  ],
});
