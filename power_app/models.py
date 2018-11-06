from django.db import models


class Project(models.Model):
    # Auto updated when data is inserted
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # Auto updated when data is altered
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    # Project Name
    name = models.CharField(max_length=255, null=True)
    # Project Duration (in days)
    duration = models.IntegerField(default=0)
    # Input Power
    power_in = models.IntegerField(default=0)
    # Output Power
    power_out = models.IntegerField(default=0)
    # Energy
    energy = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:   # To Display the name in Admin Panel
        verbose_name_plural = "Power Projects"


class Service(models.Model):
    # Auto updated when data is inserted
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # Auto updated when data is altered
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    # Project (foreign key) under which services will be available
    project = models.ForeignKey("Project", on_delete=models.CASCADE,
                                null=False)
    # Service Name
    name = models.CharField(max_length=255, null=True)
    # Service Mode
    mode = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name

    class Meta:   # To Display the name in Admin Panel
        verbose_name_plural = "Services"


class Value(models.Model):
    # Auto updated when data is inserted
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    # Auto updated when data is altered
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    # Service (foreign key) under which values will be available
    service = models.ForeignKey("Service", on_delete=models.CASCADE,
                                null=False)
    # Value Name
    name = models.CharField(max_length=255, null=True)
    # Value Formula
    formula = models.CharField(max_length=255, null=True)
    # Excel File
    file = models.FileField(upload_to='excel')

    def __str__(self):
        return self.name

    class Meta:   # To Display the name in Admin Panel
        verbose_name_plural = "Values"
