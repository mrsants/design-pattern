import { VehicleProtocol } from "./vehicle-protocol";

export class EnterpriseCar implements VehicleProtocol {
  pickUp(): void {
    throw new Error("Method not implemented.");
  }
}
