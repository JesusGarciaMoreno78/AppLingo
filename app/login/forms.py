from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField
from flask_wtf.file import FileRequired, FileAllowed, FileField
from wtforms.validators import DataRequired, Length, ValidationError


class LoginForm(FlaskForm):
    username = StringField(label="Nombre de usuario", validators=[
        DataRequired(message="El nombre de usuario es obligatorio"),
        Length(max=20, message="El nombre de usuario no puede ser superior a 20 caracteres")
    ])

    password = PasswordField(label="Contraseña", validators=[
        DataRequired(message="La contraseña es obligatoria"),
        Length(min=8, message="La contraseña no puede ser inferior a 8 caracteres")
    ])


class UsuarioForm(FlaskForm):

    username = StringField(label="Nombre de usuario", validators=[
        DataRequired(message="El nombre de usuario es obligatorio"),
        Length(max=20, message="El nombre de usuario no puede ser superior a 20 caracteres")
    ])

    password = PasswordField(label="Contraseña", validators=[
        DataRequired(message="La contraseña es obligatoria"),
        Length(min=8, message="La contraseña no puede ser inferior a 8 caracteres")
    ])
    passwordRepeat = PasswordField(label="Repita la contraseña", validators=[
        DataRequired(message="La repetición de la contraseña es obligatoria"),
        Length(min=8, message="La contraseña no puede ser inferior a 8 caracteres")
    ])

    dni = StringField(label="DNI", validators=[
        DataRequired(message="El dni es obligatorio"),
        Length(max=10, message="El dni no puede ser superior a 10 caracteres")
        ])

    nombre = StringField(label="Nombre", validators=[
        DataRequired(message="El nombre es obligatorio"),
        Length(max=20, message="El nombre no puede ser superior a 10 caracteres")
        ])

    apellidos = StringField(label="Apellidos", validators=[
        DataRequired(message="Los apellidos son obligatorio"),
        Length(max=50, message="Los apellidos no pueden superar los 50 caracteres")
        ])
    telefono = StringField(label="Telefono", validators=[
        DataRequired(message="El telfono es obligatorio"),
        Length(max=9, min=9, message="Debe tener 9 digitos")
        ])
    telefonoAlternativo = StringField(label="Telefono alternativo", validators=[
        DataRequired(message="El telfono es obligatorio"),
        Length(max=9, min=9, message="Debe tener 9 digitos")
    ])
    email = StringField(label="e-mail", validators=[
        DataRequired(message="Debe rellenar el e-mail")
    ])
    direccion = StringField(label="Dirección", validators=[
        DataRequired(message="Debe rellenar ete campo")
    ])
    # submit = SubmitField(label="Dar de alta")

    def validate_password(form,field):
        if str(field.data).isdigit():
            raise ValidationError("La contraseña no pueden ser solo dígitos")
        if field.data != form.passwordRepeat.data:
            raise ValidationError("No coinciden las contraseñas")

    def validate_passwordRepeat(form, field):
        if field.data != form.password.data:
            raise ValidationError("No coinciden las contraseñas")