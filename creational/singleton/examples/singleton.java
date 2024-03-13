public class Singleton {
    private static Singleton instance;

    private Singleton() {
        // Construtor privado para impedir a criação de instâncias fora da classe
    }

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }

    public void showMessage() {
        System.out.println("Hello World!");
    }

    public static void main(String[] args) {
        Singleton singleton1 = Singleton.getInstance();
        Singleton singleton2 = Singleton.getInstance();

        System.out.println(singleton1 == singleton2); // Saída: true

        singleton1.showMessage(); // Saída: Hello World!
    }
}
