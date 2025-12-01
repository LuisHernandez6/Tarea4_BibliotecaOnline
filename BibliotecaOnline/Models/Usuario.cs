using System.ComponentModel.DataAnnotations;

namespace BibliotecaOnline.Models
{
    public class Usuario
    {
        [Key]
        public int Id { get; set; }

        [Required]
        [MaxLength(50)]
        public string NombreUsuario { get; set; }

        [Required]
        [MaxLength(100)]
        public string Password { get; set; }

        [Required]
        [MaxLength(100)]
        public string Email { get; set; }

        // Rol: Admin o Cliente
        [Required]
        [MaxLength(20)]
        public string Rol { get; set; }
    }
}
