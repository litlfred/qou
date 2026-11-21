import { remark } from "../../schema/builders";

export default remark({
  interprets: "conj:vorticity-lower-bound",
  label: "rem:vorticity-lower-bound-argument",
  title: "Biot--Savart dynamics and vorticity concentration behind the lower bound",
  uses: ["conj:vorticity-lower-bound"],
  tags: ["vorticity", "biot-savart", "anti-parallel", "interpretation"],
});
