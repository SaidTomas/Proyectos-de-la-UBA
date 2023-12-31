package aed;

public class SistemaCNE {
    private String[] nombresPartidos;
    private String[] nombresDistritos;
    private int[] diputadosPorDistrito;
    private int[][] rangoMesasDistritos;
    private int[] votosPresidenciales;
    private int[][] votosDiputados;
    private Heap[] heap;
    private int cantVotosFst;
    private int cantVotosSec;
    private int votosTotales;
    private int[] votosPorDistrito;
    private boolean[] distritosRegistrados;
    private int[][] resultadosDiputados;
    private int[] arribaUmbralPorDistrito;

    /*
     * INVREP:
     * Primero analizamos el tamaño de los arreglos:
     * Tanto nombresDistritos , rangoMesasDistrito , votosDiputados ,
     * resultadosDiputados , diputadosPorDistrito , votosPresidenciales ,
     * distritosRegistrados , arribaUmbralPorDistrito , votosPorDistrito , heap,
     * rangoMesasDistritos tienen la misma longitud y corresponden entre sí. //! Que
     * quiere decir corresponden entre si?
     * Las longutudes de nombresPartidos y nombresDiputados son moyores a uno y no
     * tienen eltos repetidos. //! nombresDiputados no esta definida
     * 0 <= cantVotosSec <= cantVotosFst <= votosTotales.
     * forall i : nat :: 0<= i<|heap| ==>L |heap[i]|=|nombresPartidos|
     * forall i : nat :: o <= i < |rangoMesasDistritos|-1 ==>L
     * rangoMesasDistritos[i] < rangoMesasDistritos[i+1]
     * cantVotosFst es el elto mas grande de votosPresidenciales y cantVotosSec es el 
     * segundo valor mas grande de votosPresidenciales.
     * votosTotales es la suma de todos los votos (eltos) en votosPresidenciales.
     *     
     */

    public class VotosPartido {
        private int presidente;
        private int diputados;

        VotosPartido(int presidente, int diputados) {
            this.presidente = presidente;
            this.diputados = diputados;
        } // O(1)

        public int votosPresidente() {
            return presidente;
        } // O(1)

        public int votosDiputados() {
            return diputados;
        } // O(1)
    }

    public SistemaCNE(String[] nombresDistritos, int[] diputadosPorDistrito, String[] nombresPartidos,
            int[] ultimasMesasDistritos) {

        this.nombresPartidos = nombresPartidos; // O(1)
        this.nombresDistritos = nombresDistritos; // O(1)
        this.diputadosPorDistrito = diputadosPorDistrito; // O(1)

        int P = nombresPartidos.length; // O(1)
        int D = nombresDistritos.length; // O(1)

        rangoMesasDistritos = new int[D][]; // O(D)
        votosDiputados = new int[D][P]; // O(P*D)
        votosPresidenciales = new int[P]; // O(P)

        heap = new Heap[D]; // O(D)
        distritosRegistrados = new boolean[D]; // O(D)
        resultadosDiputados = new int[D][P]; // O(P*D)
        votosPorDistrito = new int[D]; // O(D)
        arribaUmbralPorDistrito = new int[D]; // O(D)

        for (int i = 0; i < D; i++) { // O(D*P)
            if (i == 0)
                rangoMesasDistritos[i] = new int[] { 0, ultimasMesasDistritos[i] }; // O(1)
            else
                rangoMesasDistritos[i] = new int[] { ultimasMesasDistritos[i - 1], ultimasMesasDistritos[i] }; // O(1)
            heap[i] = new Heap(); // O(1)
            heap[i].crearHeap(P); // O(P)
        }
    }
    /*
     * La complejidad de este programa es O(P*D) porque se definen dos matrices de
     * tamaño PxD.
     * El resto de las variables suman una complejidad menor, por lo que no se las
     * considera,
     * y el bucle tiene complejidad O(D), que es menor que O(P*D)
     */

    public String nombrePartido(int idPartido) {
        return nombresPartidos[idPartido];
    }

    public String nombreDistrito(int idDistrito) {
        return nombresDistritos[idDistrito];
    }

    public int diputadosEnDisputa(int idDistrito) {
        return diputadosPorDistrito[idDistrito];
    }
    /*
     * La complejidad de estos programas es O(1) ya que se realiza una operación
     * constante independientemente del tamaño de los datos de entrada,
     * por que la función simplemente accede a un elemento específico en el arreglo
     * y esto toma un tiempo constante y no depende del tamaño del mismo.
     */

    public String distritoDeMesa(int idMesa) {
        return nombreDistrito(busquedaBinariaRangos(rangoMesasDistritos, idMesa));
    }

    public int busquedaBinariaRangos(int[][] listaDeRangos, int obj) {
        int low = 0;
        int high = listaDeRangos.length;
        int res = -1;
        while (low <= high) {
            int mid = low + ((high - low) / 2);
            if (listaDeRangos[mid][1] <= obj) {
                low = mid + 1;
            } else if (listaDeRangos[mid][0] > obj) {
                high = mid - 1;
            } else if (estaEnDistrito(listaDeRangos[mid], obj)) {
                res = mid;
                break;
            }
        }
        return res;
    }

    public boolean estaEnDistrito(int[] tup, int n) {
        return n >= tup[0] && n < tup[1];
    }

    /*
     * La complejidad de distritoDeMesa es O(log(D)) debido al uso de búsqueda
     * binaria en la función búsquedaBinariaRangos.
     * Dado que la búsqueda binaria opera en tiempo logarítmico en el tamaño de los
     * datos (en este caso, el número de distritos),
     * la complejidad de busquedaBinariaRangos es O(log(D)).
     * La función nombreDistrito realiza una búsqueda en un arreglo de nombres de
     * distritos indexando, por lo tanto es O(1)
     * Dado que ambas operaciones se ejecutan en secuencia, la complejidad total es
     * la suma de las complejidades individuales, que en este caso es O(log(D)) +
     * O(1).
     * Nos quedamos con el término dominante, que es O(log(D)). Por lo tanto,
     * la complejidad de la línea es O(log(D))
     */

    public void registrarMesa(int idMesa, VotosPartido[] actaMesa) {
        int P = nombresPartidos.length;
        int distrito = busquedaBinariaRangos(rangoMesasDistritos, idMesa);
        cantVotosFst = 0;
        cantVotosSec = 0;
        votosTotales = 0;
        for (int i = 0; i < P; i++) {
            votosPorDistrito[distrito] += votosDiputados[distrito][i];
            votosPresidenciales[i] += actaMesa[i].votosPresidente();
            votosDiputados[distrito][i] += actaMesa[i].votosDiputados();

            if (cantVotosFst < votosPresidenciales[i]) {
                cantVotosSec = cantVotosFst;
                cantVotosFst = votosPresidenciales[i];

            }
            if (votosPresidenciales[i] < cantVotosFst && cantVotosSec < votosPresidenciales[i]) {
                cantVotosSec = votosPresidenciales[i];
            }
            votosTotales = votosTotales + votosPresidenciales[i];
        }

        for (int j = 0; j < P - 1; j++) {
            if (votosDiputados[distrito][j] * 100 / ((float) votosPorDistrito[distrito]) > 3) {
                arribaUmbralPorDistrito[distrito] += 1;
            }
        }

        int l = 0;
        for (int h = 0; h < P - 1; h++) {
            if (votosDiputados[distrito][h] * 100 / ((float) votosPorDistrito[distrito]) >= 3) {
                int[] r = new int[2]
                r[0] = votosDiputados[distrito][l];
                r[1] = l;
                heap[distrito].encolar(r);
                l += 1;
            }
        }
    }

    /*
     * La complejidad de registrarMesa es O(P + log(D)) ya que primero se utiliza el
     * algoritmo de busquedaBinariaRangos para definir la variable "distrito"
     * (O(log(D))
     * y luego le siguen 3 ciclos que iteran de 0 a P y dentro de ellos se
     * encuentran operaciones de complejidad O(1). Por lo tanto me queda O(3P +
     * log(D)) = O(P + log(D)). 
     * 
     */

    public int votosPresidenciales(int idPartido) {
        return this.votosPresidenciales[idPartido];
    }

    public int votosDiputados(int idPartido, int idDistrito) {
        return this.votosDiputados[idDistrito][idPartido];
    }
    /*
     * La complejidad de estos programas es O(1) ya que se realiza una operación
     * constante independientemente del tamaño de los datos de entrada,
     * por que la función simplemente accede a un elemento específico en el arreglo
     * y esto toma un tiempo constante y no depende del tamaño del mismo.
     */

    public int[] resultadosDiputados(int idDistrito) {
        int bancas = diputadosPorDistrito[idDistrito];
        int reparti = 0;
        if (!distritosRegistrados[idDistrito]) {
            while (reparti < bancas) {
                int[] max = heap[idDistrito].repr[0];
                resultadosDiputados[idDistrito][max[1]] += 1;
                reparti += 1;
                heap[idDistrito].repr[0][0] = votosDiputados[idDistrito][max[1]] / (resultados[max[1]] + 1);
                heap[idDistrito].bajar(0);
            }
            distritosRegistrados[idDistrito] = true;
            resultadosDiputados[idDistrito] = resultados;
        } 
        return resultadosDiputados[idDistrito];
    }

    /*
     * La complejidad de este programa es O(Dd * log(P)), donde Dd es la cantidad de
     * bancas de diputados en el distrito d y P es la cantidad de partidos
     * ya que el bucle del while se ejecuta hasta que se hayan repartido todas las
     * bancas en el distrito d, y el número de bancas en el distrito es Dd,
     * donde en cada iteración , se realiza una operación de inserción y extracción
     * en un heap (estructura de datos), que tiene una complejidad logarítmica
     * en el número de elementos en el heap. En este caso, el número de elementos en
     * el heap está relacionado con la cantidad de partidos (P).
     * Dado que el bucle while ejecuta un número máximo de veces igual a la cantidad
     * de bancas (Dd), y en cada iteración se realiza una operación de complejidad
     * logarítmica en P, la complejidad total es O(Dd * log(P)).
     */

    public boolean hayBallotage() {
        float porcentajePrimero = (((float) cantVotosFst) * (float) 100 / (float) votosTotales);
        float porcentajeSegundo = ((float) cantVotosSec * (float) 100 / (float) votosTotales);
        if (porcentajePrimero > 45.0) {
            return false;
        } else if (porcentajePrimero > 40.0 && porcentajePrimero - porcentajeSegundo > 10) {
            return false;
        } else {
            return true;
        }
    }
}
/*
 * La complejidad de este programa es O(1) porque no involucra ningún bucle ni
 * iteración que dependa del tamaño de los datos.
 * En su lugar, realiza operaciones matemáticas simples en tiempo constante para
 * calcular los porcentajes y compararlos.
 * Estas operaciones son independientes del tamaño de los datos, lo que conduce
 * a una complejidad constante O(1).
 */
