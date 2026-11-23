import { theorem } from "../../schema/builders";

export default theorem({
  label: "thm:diophantine-birthday-trajectory",
  title:
    "The birthday-trajectory separation: impossible at the birthday, unobstructed at the trajectory, and blocked only by a quantifier",
  tags: [
    "surreal-numbers",
    "birthday",
    "sign-expansion",
    "diophantine",
    "liouville",
    "roth",
    "gonshor",
    "dyadic-approximation",
  ],
  lean: {
    ref: "qou:QOU.AppendixSurreals.liouvilleWith_separates",
    validation: "leanok",
  },
  uses: [
    // conj:diophantine-birthday removed (qou-tm3c): the conjecture is the block's subject, not a premise. The claims are classical and proved in DiophantineBirthdayTrajectory.lean (rational-shift invariance, runs imply LiouvilleWith); Roth enters as a stated hypothesis.
  ],
  cites: ["conway1976", "gonshor1986"],
  authorNotes: [
    { kind: "note", date: "2026-11-20", body: "Relocated from the block prose by the voice-leak drain (qou-d4kh, option 3): Original wording: Liouville's theorem \"is fully formalised, with $\\sum 2^{-n!}$ as a concrete witness\"; \"Roth proved it in 1955. What is missing is a *formalisation*, not a proof\"." },
  ],
});
