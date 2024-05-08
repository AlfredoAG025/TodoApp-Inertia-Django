from marshmallow import Schema, fields, validate


class NoteSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(
        validate=validate.Length(min=1, max=50),
        error="Title must be between 1 and 50 characters",
    )
    content = fields.Str(
        validate=validate.Length(min=1, max=255),
        error="Content must be between 1 and 255 characters",
    )
    color = fields.Str()
    timestamp = fields.DateTime()
    is_favorite = fields.Boolean()
