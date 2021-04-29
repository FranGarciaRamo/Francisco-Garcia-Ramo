package MiCodigo;

public class PaísEuropeo extends País{
	private String europeo;
	public PaísEuropeo(String nombre, String idioma, Double terreno, Double poblacion) {
		super(nombre, idioma, terreno, poblacion);
		// TODO Auto-generated constructor stub
	}
	/**
	 * @return the europeo
	 */
	public String getEuropeo() {
		return europeo;
	}
	/**
	 * @param europeo the europeo to set
	 */
	public void setEuropeo(String europeo) {
		this.europeo = europeo;
	}
	
	
	 
}
