export class Singleton {
    private static _instance: Singleton | null = null

    private constructor() {
        // new not allowed outside the class
    }

    static get instance(): Singleton {
        if(Singleton._instance === null) {
            Singleton._instance = new Singleton()
        }
        return Singleton._instance;
    }
}

const instance1 = new Singleton.instance;
const instance2 = new Singleton.instance;

console.log(instance1 === instance2)