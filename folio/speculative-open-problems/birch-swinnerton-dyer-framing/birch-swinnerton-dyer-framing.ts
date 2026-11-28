import { chapter, section } from "../../schema/builders";

export default chapter({
  title: "Birch and Swinnerton-Dyer Framing",
  label: "chap:birch-swinnerton-dyer-framing",
  sections: [
    section({
      title: "Categorical Hom-groups versus arithmetic Mordell--Weil rank",
      label: "sec:bsd-framing",
      blocks: [
        "bsd-framing-intro",
        "q-birch-swinnerton-dyer",
        "q-bsd-rank-zero",
        "q-bsd-classical-limit",
        "bsd-surreal-bound",
        "adelic-tate-bsd-reduction",
      ],
    }),
  ],
});
