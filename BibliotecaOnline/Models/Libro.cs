using System.ComponentModel.DataAnnotations;

namespace BibliotecaOnline.Models
{
    public class Libro
    {
        public int Id { get; set; }

        [Required]
        public string Titulo { get; set; }

        [Required]
        public string Autor { get; set; }

        [Required]
        public decimal Precio { get; set; }

        [Required]
        public int Stock { get; set; }
    }
}
