def main(env):
    fields = env['ir.model.fields'].search([])
    for field in fields:
        field.model_id.name
