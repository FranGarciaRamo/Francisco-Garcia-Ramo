package MiCodigo;

public class País {
	private String nombre;
	private String idioma;
	private Double terreno;
	private Double poblacion;
	public País(String nombre, String idioma, Double terreno, Double poblacion) {
		super();
		this.nombre = nombre;
		this.idioma = idioma;
		this.terreno = terreno;
		this.poblacion = poblacion;
	}
	
	public Double getTerreno() {
		return terreno;
	}
	/**
	 * @param terreno the terreno to set
	 */
	public void setTerreno(Double terreno) {
		this.terreno = terreno;
	}
	/**
	 * @return the poblacion
	 */
	public Double getPoblacion() {
		return poblacion;
	}
	/**
	 * @param poblacion the poblacion to set
	 */
	public void setPoblacion(Double poblacion) {
		this.poblacion = poblacion;
	}

	/**
	 * @return the idioma
	 */
	public String getIdioma() {
		return idioma;
	}

	/**
	 * @param idioma the idioma to set
	 */
	public void setIdioma(String idioma) {
		this.idioma = idioma;
	}

	public País(String nombre) {
		super();
		this.nombre = nombre;
	}

	/**
	 * @return the nombre
	 */
	public String getNombre() {
		return nombre;
	}

	/**
	 * @param nombre the nombre to set
	 */
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}

	/**
	 * @return the nombre
	 */



}
